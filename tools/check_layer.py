import os

def check_structure():
    required_paths = [
        "meta-yocto-lab/conf/layer.conf",
        "meta-yocto-lab/recipes-apps/hello/hello_1.0.bb",
        "meta-yocto-lab/recipes-apps/hello/files/hello.sh",
        "samples/bblayers.conf",
        "samples/local.conf"
    ]

    for path in required_paths:
        if not os.path.exists(path):
            print(f"Error: Required file not found: {path}")
            return False
    print("Layer and config structure check passed!")
    return True

if __name__ == "__main__":
    check_structure()
