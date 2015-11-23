
//-------------------------------------------------------------------------------------------------------------------------------
#include <vector>
#include <string>
#include <iomanip>
#include <sstream>
#include <stdint.h>
#include <iostream>
#include <dirent.h>
#include <exception>
#include <boost/regex.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/ini_parser.hpp>

//-------------------------------------------------------------------------------------------------------------------------------
using namespace std;

//-------------------------------------------------------------------------------------------------------------------------------
typedef struct
{
  bool enable;
  struct
  {
    struct
    {
      bool enable;
      string value;
    } eipoib_mac_address;
    string infiniband;
    string ethernet;
    string eipoib;
    string port;
    string virtfn;
  } prefix;
  struct
  {
    int32_t card;
    int32_t port;
    int32_t virtfn;
  } limit;
} udev_namer_config;

//-------------------------------------------------------------------------------------------------------------------------------
typedef struct
{
  struct {
    int32_t num;
  } card;
  struct
  {
    string bus;
    string type;
    string interface;
    string value;
  } path;
  struct
  {
    int32_t num;
    struct
    {
      int32_t bus_type;
      int32_t net_type;
    } link;
  } port;
  struct
  {
    string bus;
    int32_t num;
  } virtfn;
} udev_namer_param;

//-------------------------------------------------------------------------------------------------------------------------------
static const char*          RANDOM_CHAR_DEVICE                              = "/dev/urandom";
static const string         IP_LINK_TOKEN_DEV                               = "ip link set dev";
static const string         IP_LINK_TOKEN_ADDRESS                           = "address";
static const string         IP_LINK_TOKEN_DOWN                              = "down";
static const string         IP_LINK_TOKEN_UP                                = "up";
static const string         IP_LINK_TOKEN_NO_OUT                            = "> /dev/null 2>&1";

static const char*          CONFIG_FILE                                     = "/etc/udev/mlnx-udev-namer.conf";
static const char*          CONFIG_VARIABLE_ENABLE                          = "enable";
static const bool           CONFIG_DEFAULT_ENABLE                           = false;
static const char*          CONFIG_VARIABLE_GENERATE_EIPOIB_MAC_ADDRESS     = "generate_eipoib_mac_address";
static const bool           CONFIG_DEFAULT_GENERATE_EIPOIB_MAC_ADDRESS      = false;
static const char*          CONFIG_VARIABLE_PREFIX_EIPOIB_MAC_ADDRESS       = "prefix_eipoib_mac_address";
static const char*          CONFIG_DEFAULT_PREFIX_EIPOIB_MAC_ADDRESS        = "fe";
static const char*          CONFIG_VARIABLE_PREFIX_INERFACE_INFINIBAND      = "prefix_infiniband";
static const char*          CONFIG_DEFAULT_PREFIX_INERFACE_INFINIBAND       = "ib";
static const char*          CONFIG_VARIABLE_PREFIX_INERFACE_ETHERNET        = "prefix_ethernet";
static const char*          CONFIG_DEFAULT_PREFIX_INERFACE_ETHERNET         = "me";
static const char*          CONFIG_VARIABLE_PREFIX_INERFACE_EIPOIB          = "prefix_eipoib";
static const char*          CONFIG_DEFAULT_PREFIX_INERFACE_EIPOIB           = "mi";
static const char*          CONFIG_VARIABLE_PREFIX_INERFACE_PORT            = "prefix_port";
static const char*          CONFIG_DEFAULT_PREFIX_INERFACE_PORT             = "p";
static const char*          CONFIG_VARIABLE_PREFIX_INERFACE_VIRTFN          = "prefix_virtfn";
static const char*          CONFIG_DEFAULT_PREFIX_INERFACE_VIRTFN           = "f";
static const int32_t        CONFIG_LIMIT_CARD_NUMBER                        = 64;
static const int32_t        CONFIG_LIMIT_PORT_PER_CARD_NUMBER               = 64;
static const int32_t        CONFIG_LIMIT_VIRTFN_PER_CARD_NUMBER             = 2048;

static const char*          UDEV_DEV_ENV_DEVPATH                            = "DEVPATH";
static const string         UDEV_DEV_VENDOR_ID                              = "15b3";
static const string         UDEV_DEV_SYS_CLASS_TYPE                         = "net";
static const int32_t        UDEV_DEV_NOT_DEFINED                            = -1;
static const int32_t        UDEV_DEV_LINK_TYPE_ETHERNET                     = 1;
static const int32_t        UDEV_DEV_LINK_TYPE_INFINIBAND                   = 32;
static const string         UDEV_DIR_SYS_PCI_DEVICES                        = "/sys/bus/pci/devices";
static const string         UDEV_DIR_SYS_CLASS_NET                          = "/sys/class/net";
static const string         UDEV_LINK_PHYS_FN                               = "physfn";
static const string         UDEV_LINK_VIRT_FN_PCI_BUS                       = "virtfn";
static const string         UDEV_FILE_SRIOV_NUMVFS                          = "sriov_numvfs";
static const string         UDEV_FILE_VENDOR                                = "vendor";
static const string         UDEV_FILE_DEVICE                                = "device";
static const string         UDEV_FILE_DEVICE_ID                             = "dev_id";
static const string         UDEV_FILE_DEVICE_PORT                           = "dev_port";
static const string         UDEV_FILE_TYPE                                  = "type";
static const string         UDEV_FILE_PORT_PREFIX                           = "mlx4_port";

//-------------------------------------------------------------------------------------------------------------------------------
static const boost::regex   REGEX_PCI_BUS(                                    "^[[:xdigit:]]{4}(:[[:xdigit:]]{2}){2}\\.[[:xdigit:]]$");
static const boost::regex   REGEX_PCI_BUS_FROM_PATH(                          "^(.*/)([[:xdigit:]]{4}(:[[:xdigit:]]{2}){2}\\.[[:xdigit:]])$");
static const boost::regex   REGEX_PHYS_LINK_LAYER_IS_ETH(                     "^(auto *\\()*eth(\\))*$");
static const boost::regex   REGEX_PHYS_LINK_LAYER_IS_IB(                      "^(auto *\\()*ib(\\))*$");
static const boost::regex   REGEX_PARAM_VAL_IS_MAC_ADDRESS_PREFIX(            "^(([[:xdigit:]]{2})(:)){0,3}([[:xdigit:]]){1,2}$");
static const boost::regex   REGEX_PARAM_VAL_IS_TRUE(                          "^(true|yes)$", boost::regex::icase);
static const boost::regex   REGEX_PARAM_VAL_IS_FALSE(                         "^(false|no)$", boost::regex::icase);
static const boost::regex   REGEX_PARAM_VAL_IS_INTERFACE_PREFIX(              "^[[:alpha:]][[:alpha:]\\-_]{0,3}$");
static const boost::regex   REGEX_PARAM_VAL_IS_INTERFACE_TOKEN_PREFIX(        "^[[:alpha:]]{1,2}$");
static const boost::regex   REGEX_ENV_DEVPATH(                                "^(.*/+)([[:xdigit:]]{4}(:[[:xdigit:]]{2}){2}\\.[[:xdigit:]])(/+)([[:alpha:]][[:alnum:]]*)(/+)([[:alpha:]][[:alnum:]]*)$");

//-------------------------------------------------------------------------------------------------------------------------------
void config_set_eipoib_mac_address(udev_namer_config& conf, const char* prefix)
{
  string& s = conf.prefix.eipoib_mac_address.value;
  s.assign(CONFIG_DEFAULT_PREFIX_EIPOIB_MAC_ADDRESS);
  if (boost::regex_match(prefix, REGEX_PARAM_VAL_IS_MAC_ADDRESS_PREFIX))
    s.assign(prefix);
  s.erase(remove(s.begin(), s.end(), ':'), s.end());
  transform(s.begin(), s.end(), s.begin(), ::tolower);
}

//-------------------------------------------------------------------------------------------------------------------------------
void config_set_default(udev_namer_config& conf)
{
  conf.enable                            = CONFIG_DEFAULT_ENABLE;
  conf.prefix.eipoib_mac_address.enable  = CONFIG_DEFAULT_GENERATE_EIPOIB_MAC_ADDRESS;
  conf.limit.card                        = CONFIG_LIMIT_CARD_NUMBER;
  conf.limit.port                        = CONFIG_LIMIT_PORT_PER_CARD_NUMBER;
  conf.limit.virtfn                      = CONFIG_LIMIT_VIRTFN_PER_CARD_NUMBER;
  conf.prefix.infiniband.assign(           CONFIG_DEFAULT_PREFIX_INERFACE_INFINIBAND);
  conf.prefix.ethernet.assign(             CONFIG_DEFAULT_PREFIX_INERFACE_ETHERNET);
  conf.prefix.eipoib.assign(               CONFIG_DEFAULT_PREFIX_INERFACE_EIPOIB);
  conf.prefix.port.assign(                 CONFIG_DEFAULT_PREFIX_INERFACE_PORT);
  conf.prefix.virtfn.assign(               CONFIG_DEFAULT_PREFIX_INERFACE_VIRTFN);
  config_set_eipoib_mac_address(     conf, CONFIG_DEFAULT_PREFIX_EIPOIB_MAC_ADDRESS);
}

//-------------------------------------------------------------------------------------------------------------------------------
void config_get_bool_value_from_file(boost::property_tree::ptree pt, bool& var_conf,
  const char* var_name)
{
  string value;
  boost::property_tree::ptree::const_assoc_iterator it = pt.find(var_name);
  if (it != pt.not_found()) value = pt.get<std::string>(var_name);

  if (boost::regex_match(value.c_str(), REGEX_PARAM_VAL_IS_TRUE)) var_conf = true;
  if (boost::regex_match(value.c_str(), REGEX_PARAM_VAL_IS_FALSE)) var_conf = false;
}

//-------------------------------------------------------------------------------------------------------------------------------
void config_get_string_value_from_file(boost::property_tree::ptree pt, string& var_conf,
  const char* var_name, const boost::regex& var_regex, bool to_lower = true)
{
  string value;
  boost::property_tree::ptree::const_assoc_iterator it = pt.find(var_name);
  if (it != pt.not_found()) value = pt.get<std::string>(var_name);
  if (boost::regex_match(value.c_str(), var_regex))
  {
    var_conf = value;
    if (to_lower) transform(var_conf.begin(), var_conf.end(), var_conf.begin(), ::tolower);
  }
}

//-------------------------------------------------------------------------------------------------------------------------------
void config_read_from_file(udev_namer_config& conf)
{
  config_set_default(conf);
  ifstream conf_file(CONFIG_FILE);
  if (conf_file.is_open())
  {
    conf_file.close();
    boost::property_tree::ptree pt;
    boost::property_tree::ini_parser::read_ini(CONFIG_FILE, pt);
    
    config_get_bool_value_from_file(pt, conf.enable, CONFIG_VARIABLE_ENABLE);

    if (conf.enable)
    {
      config_get_bool_value_from_file
      (
        pt,
        conf.prefix.eipoib_mac_address.enable,
        CONFIG_VARIABLE_GENERATE_EIPOIB_MAC_ADDRESS
      );

      if (conf.prefix.eipoib_mac_address.enable)
      {
        string s = "";
        boost::property_tree::ptree::const_assoc_iterator it = pt.find(CONFIG_VARIABLE_PREFIX_EIPOIB_MAC_ADDRESS);
        if (it != pt.not_found()) s = pt.get<std::string>(CONFIG_VARIABLE_PREFIX_EIPOIB_MAC_ADDRESS);
        config_set_eipoib_mac_address(conf, s.c_str());
      }

      config_get_string_value_from_file
      (
        pt,
        conf.prefix.infiniband,
        CONFIG_VARIABLE_PREFIX_INERFACE_INFINIBAND,
        REGEX_PARAM_VAL_IS_INTERFACE_PREFIX
      );

      config_get_string_value_from_file
      (
        pt,
        conf.prefix.ethernet,
        CONFIG_VARIABLE_PREFIX_INERFACE_ETHERNET,
        REGEX_PARAM_VAL_IS_INTERFACE_PREFIX
      );

      config_get_string_value_from_file
      (
        pt,
        conf.prefix.eipoib,
        CONFIG_VARIABLE_PREFIX_INERFACE_EIPOIB,
        REGEX_PARAM_VAL_IS_INTERFACE_PREFIX
      );

      config_get_string_value_from_file
      (
        pt,
        conf.prefix.port,
        CONFIG_VARIABLE_PREFIX_INERFACE_PORT,
        REGEX_PARAM_VAL_IS_INTERFACE_TOKEN_PREFIX
      );

      config_get_string_value_from_file
      (
        pt,
        conf.prefix.virtfn,
        CONFIG_VARIABLE_PREFIX_INERFACE_VIRTFN,
        REGEX_PARAM_VAL_IS_INTERFACE_TOKEN_PREFIX
      );
    }
  }
}

//-------------------------------------------------------------------------------------------------------------------------------
bool is_pci_bus(string& s)
{
  return boost::regex_match(s.c_str(), REGEX_PCI_BUS);
}

//-------------------------------------------------------------------------------------------------------------------------------
bool read_string_from_file(const char* f, string& s)
{
  bool rc;
  ifstream file(f);
  if ((rc = file.is_open()))
  {
    rc = getline(file, s);
    file.close();
  }
  return rc;
}

//-------------------------------------------------------------------------------------------------------------------------------
bool param_set_default(udev_namer_param& param)
{
  param.path.bus                = "";
  param.path.type               = "";
  param.path.interface          = "";
  param.path.value              = "";
  param.card.num                = UDEV_DEV_NOT_DEFINED;
  param.port.num                = UDEV_DEV_NOT_DEFINED;
  param.port.link.bus_type      = UDEV_DEV_NOT_DEFINED;
  param.port.link.net_type      = UDEV_DEV_NOT_DEFINED;
  param.virtfn.bus              = "";
  param.virtfn.num              = UDEV_DEV_NOT_DEFINED;
  return false;
}

//-------------------------------------------------------------------------------------------------------------------------------
string read_link(const char* f)
{
  string rs = "";
  char buffer[PATH_MAX];
  ssize_t len = ::readlink(f, buffer, sizeof(buffer) - 1);
  if (len != -1)
  {
    buffer[len] = '\0';
    rs.assign(buffer);
  }
  return rs;    
}

//-------------------------------------------------------------------------------------------------------------------------------
bool param_read(udev_namer_config& conf, udev_namer_param& param)
{
  param_set_default(param);
  const char* devpath = getenv(UDEV_DEV_ENV_DEVPATH);

  if (devpath == NULL)
        return false;
  
  boost::cmatch m;

  if (! boost::regex_match(devpath, m, REGEX_ENV_DEVPATH))
        return false;
  
  param.path.bus        = boost::lexical_cast<string>(m[2]);
  param.path.type       = boost::lexical_cast<string>(m[5]);
  param.path.interface  = boost::lexical_cast<string>(m[7]);

  if (param.path.type != UDEV_DEV_SYS_CLASS_TYPE || ! is_pci_bus(param.path.bus))
        return param_set_default(param);

  param.path.value.assign(devpath);
  string string_form_file;

  if ( ! read_string_from_file((UDEV_DIR_SYS_PCI_DEVICES + "/" + param.path.bus + "/" + UDEV_FILE_VENDOR).c_str(), string_form_file) || 
    string_form_file != "0x" + UDEV_DEV_VENDOR_ID)
        return param_set_default(param);

  if (read_string_from_file((UDEV_DIR_SYS_CLASS_NET + "/" + param.path.interface + "/" + UDEV_FILE_DEVICE_PORT).c_str(), string_form_file))
    param.port.num = atoi(string_form_file.c_str());
  else if (read_string_from_file((UDEV_DIR_SYS_CLASS_NET + "/" + param.path.interface + "/" + UDEV_FILE_DEVICE_ID).c_str(), string_form_file))
    param.port.num = strtol(string_form_file.c_str(), NULL, 16);
  else  
        return param_set_default(param);

  if (param.port.num < 0 || param.port.num > conf.limit.port)        
        return param_set_default(param);

  if ( ! read_string_from_file((UDEV_DIR_SYS_CLASS_NET + "/" + param.path.interface + "/" + UDEV_FILE_TYPE).c_str(), string_form_file) ||
    ! ((param.port.link.net_type = atoi(string_form_file.c_str())) == UDEV_DEV_LINK_TYPE_ETHERNET ||
      param.port.link.net_type == UDEV_DEV_LINK_TYPE_INFINIBAND))
        return param_set_default(param);

  stringstream ss;
  ss << UDEV_DIR_SYS_PCI_DEVICES << "/" << param.path.bus << "/" << UDEV_FILE_PORT_PREFIX << param.port.num + 1;
  if ( ! read_string_from_file(ss.str().c_str(), string_form_file))
        return param_set_default(param);
  
  if (boost::regex_match(string_form_file.c_str(), REGEX_PHYS_LINK_LAYER_IS_ETH)) param.port.link.bus_type = UDEV_DEV_LINK_TYPE_ETHERNET; 

  if (param.port.link.bus_type == UDEV_DEV_NOT_DEFINED &&
    boost::regex_match(string_form_file.c_str(), REGEX_PHYS_LINK_LAYER_IS_IB)) param.port.link.bus_type = UDEV_DEV_LINK_TYPE_INFINIBAND; 

  if (param.port.link.bus_type == UDEV_DEV_NOT_DEFINED)
        return param_set_default(param);

  bool is_virtfn = false;

  if (read_string_from_file((UDEV_DIR_SYS_PCI_DEVICES + "/" + param.path.bus + "/" + UDEV_LINK_PHYS_FN + "/" + UDEV_FILE_SRIOV_NUMVFS).c_str(), string_form_file))
  {
    is_virtfn = true;

    int num_vfs = atoi(string_form_file.c_str());
    string_form_file = read_link((UDEV_DIR_SYS_PCI_DEVICES + "/" + param.path.bus + "/" + UDEV_LINK_PHYS_FN).c_str());

    if (! boost::regex_match(string_form_file.c_str(), m, REGEX_PCI_BUS_FROM_PATH))
        return param_set_default(param);

    param.virtfn.bus = boost::lexical_cast<string>(m[2]);

    int32_t j = num_vfs;
    if (j > conf.limit.virtfn) j = conf.limit.virtfn;

    for (int32_t i = 0; i < j; i++ )
    {
      ss.str("");
      ss << UDEV_DIR_SYS_PCI_DEVICES << "/" << param.path.bus << "/" << UDEV_LINK_PHYS_FN << "/" << UDEV_LINK_VIRT_FN_PCI_BUS << i;
      string_form_file = read_link(ss.str().c_str());

      if (! boost::regex_match(string_form_file.c_str(), m, REGEX_PCI_BUS_FROM_PATH))
        return param_set_default(param);

      string_form_file = boost::lexical_cast<string>(m[2]);

      if (string_form_file == param.path.bus)
      {
        param.virtfn.num = i;
        break;
      }
    }
  }

  string phys_pci_device = param.path.bus;
  if (is_virtfn) phys_pci_device = param.virtfn.bus;

  DIR *dp;
  struct dirent *dirp;
  if ((dp  = opendir(UDEV_DIR_SYS_PCI_DEVICES.c_str())) == NULL)
        return param_set_default(param);

  int32_t j = 0;
  vector<string> pci_dev_list;
  while ((dirp = readdir(dp)) != NULL)
  {
    string dev_pci_bus = string(dirp->d_name);
    if (dev_pci_bus != "." &&
      dev_pci_bus != ".." &&
      read_string_from_file((UDEV_DIR_SYS_PCI_DEVICES + "/" + dev_pci_bus + "/" + UDEV_FILE_VENDOR).c_str(), string_form_file) &&
      string_form_file == "0x" + UDEV_DEV_VENDOR_ID && 
      ! read_string_from_file((UDEV_DIR_SYS_PCI_DEVICES + "/" + dev_pci_bus + "/" + UDEV_LINK_PHYS_FN + "/" + UDEV_FILE_SRIOV_NUMVFS).c_str(), string_form_file))
    {
      if (j++ >= conf.limit.card) break;
      pci_dev_list.push_back(dev_pci_bus);
    }
  }

  closedir(dp);
  sort(pci_dev_list.begin(), pci_dev_list.end());

  for (uint32_t i = 0; i < pci_dev_list.size(); i++)
    if (pci_dev_list[i] == phys_pci_device)
    {
      param.card.num = i;
      break;
    }

  if (param.card.num == UDEV_DEV_NOT_DEFINED)
        return param_set_default(param);

  return true;
}

//-------------------------------------------------------------------------------------------------------------------------------
string generate_eipoib_mac_address(string& prefix)
{
  string s;
  stringstream ss;
  const uint32_t MAC_ADDRES_LEN = 6;

  ifstream f(RANDOM_CHAR_DEVICE);
  if (f.is_open())
  {
    unsigned char ch;
    ss << prefix;
    for (uint32_t i = 0; i < (MAC_ADDRES_LEN - (prefix.length() / 2)); i++)
    {
      f >> ch;
      ss << setw(2) << setfill('0') << hex << (int) ch ;
    }
    f.close();
  }

  s = ss.str().substr(0, 2 * MAC_ADDRES_LEN);
  ss.str("");

  for (uint32_t i = 0; i < MAC_ADDRES_LEN; i++)
  {
    if (i != 0) ss << ":";
    ss << s.substr(2 * i, 2) ;
  }

  return ss.str();
}

//-------------------------------------------------------------------------------------------------------------------------------
int interface_set_mac_address(string& i, string m)
{
  return system((IP_LINK_TOKEN_DEV + " " + i + " " + IP_LINK_TOKEN_DOWN + " " + IP_LINK_TOKEN_NO_OUT).c_str()) +
    system((IP_LINK_TOKEN_DEV + " " + i + " " + IP_LINK_TOKEN_ADDRESS + " " + m + " " + IP_LINK_TOKEN_NO_OUT).c_str());
}

//-------------------------------------------------------------------------------------------------------------------------------
int main()
{
  udev_namer_config conf;
  config_read_from_file(conf);
  if ( ! conf.enable) exit(0);

  udev_namer_param param;
  if ( ! param_read(conf, param)) exit(0);

  stringstream ss;

  if (param.port.link.bus_type == UDEV_DEV_LINK_TYPE_ETHERNET)
    ss << conf.prefix.ethernet;
  else if (param.port.link.net_type == UDEV_DEV_LINK_TYPE_INFINIBAND)
    ss << conf.prefix.infiniband;
  else
  {
    ss << conf.prefix.eipoib;
    if (conf.prefix.eipoib_mac_address.enable && param.virtfn.num != UDEV_DEV_NOT_DEFINED)
      interface_set_mac_address(param.path.interface, generate_eipoib_mac_address(conf.prefix.eipoib_mac_address.value));
  }
  
  ss << param.card.num << conf.prefix.port << param.port.num;
  
  if (param.virtfn.num != UDEV_DEV_NOT_DEFINED)
    ss << conf.prefix.virtfn << param.virtfn.num;

  cout << ss.str() << endl;

  exit(0);
}
