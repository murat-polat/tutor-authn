from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutorauthn", "templates"
)

config = {
    "add": {
        
        "OAUTH2_SECRET": "{{ 24|random_string }}",
    },

    "defaults": {
        "HOST": "{{ LMS_HOST }}:1999",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/authn",
          }
}

hooks = {

    "init": ["lms","authn"],
    "build-image": {"authn": "muratp/authn"},
    "remote-image": {"authn": "muratp/authn"},
   
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorauthn", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
