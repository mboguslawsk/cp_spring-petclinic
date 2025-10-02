from semver import VersionInfo

import subprocess
import sys
import os

VERSION_FILE = "VERSION"

def get_current_version():
    if not os.path.exists(VERSION_FILE):
        return VersionInfo.parse("0.0.0")
    else:
        with open(VERSION_FILE) as f:
            return VersionInfo.parse(f.read().strip())


def bump_version_tag(seman_version_type):
    current_ver = get_current_version()
    if seman_version_type == "major":
        new_version = current_ver.bump_major()
    elif seman_version_type == "minor":
        new_version = current_ver.bump_minor()
    elif seman_version_type == "patch":
        new_version = current_ver.bump_patch()
    else:
        print("Please provide correct semantic version type: major, minor or patch")
        exit()
    with open(VERSION_FILE, "w") as f:
        f.write(str(new_version))

    print("\nAdding git tag ...\n")
    subprocess.run(["git", "tag", str(new_version)])
    subprocess.run(["git", "push", "--tags"])
    print(f"\nBumped version to {new_version}\n")
    return str(new_version)

if __name__ == "__main__":
    seman_version_type = sys.argv[1]
    bump_version_tag(seman_version_type)