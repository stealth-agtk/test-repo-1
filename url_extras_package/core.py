import importlib.util
import json
import os
import pathlib

def has_package(package_name):
    """Check if a package is installed."""
    return importlib.util.find_spec(package_name) is not None

def load_json_data():
    """
    Load JSON data from the json_data extra if installed.
    """
    try:
        if has_package('json_data'):
            import json_data
            data_path = pathlib.Path(json_data.__path__[0]) / 'data.json'
            with open(data_path, 'r') as f:
                return json.load(f)
        else:
            return {"error": "json_data extra is not installed"}
    except Exception as e:
        return {"error": f"Failed to load JSON data: {str(e)}"}

def use_git_component():
    """
    Use functionality from the git_component extra if installed.
    """
    if has_package('git_component'):
        import git_component
        return git_component.get_info()
    else:
        return "git_component extra is not installed"

def use_monorepo_component():
    """
    Use functionality from the monorepo_component extra if installed.
    """
    if has_package('specific_package'):
        import specific_package
        return specific_package.get_info()
    else:
        return "monorepo_component extra is not installed"
