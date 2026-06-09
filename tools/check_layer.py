import os

def check_structure():
    required_paths = [
        "meta-example/conf/layer.conf",
        "meta-example/recipes-example/hello/hello_1.0.bb",
        "meta-example/recipes-example/hello/files/hello.sh",
        "conf-examples/bblayers.conf",
        "conf-examples/local.conf"
    ]

    for path in required_paths:
        if not os.path.exists(path):
            print(f"Error: Required file not found: {path}")
            return False
    print("Layer and config structure check passed!")
    return True

if __name__ == "__main__":
    check_structure()

