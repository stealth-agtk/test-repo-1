import sys
import pkg_resources

def list_installed_extras(package_name="url_extras_package"):
    """
    List all installed extras for the package.
    """
    all_packages = {dist.key: dist for dist in pkg_resources.working_set}
    
    # Define mapping of package names to extras
    extras_mapping = {
        "numpy": "standard",
        "json_data": "json_data",
        "git_component": "git_component",
        "specific_package": "monorepo_component"
    }
    
    installed_extras = []
    
    for package, extra in extras_mapping.items():
        if package in all_packages:
            installed_extras.append(extra)
    
    return installed_extras

def check_extra(extra_name):
    """
    Check if a specific extra is installed.
    """
    return extra_name in list_installed_extras()
