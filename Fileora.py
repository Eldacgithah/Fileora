import sys
import requests
import os

def upload_to_catbox(file_path: str) -> str:
    url = "https://catbox.moe/user/api.php"
    with open(file_path, "rb") as f:
        response = requests.post(
            url,
            data={"reqtype": "fileupload"},
            files={"fileToUpload": f}
        )
    if response.ok:
        return response.text.strip()
    else:
        raise Exception(f"Upload failed: {response.text}")

def main():
    if len(sys.argv) < 2:
        print("Usage: fileora <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("Error: file not found ->", file_path)
        sys.exit(1)
    link = upload_to_catbox(file_path)
    print("File uploaded successfully")
    print("Direct link:", link)

if __name__ == "__main__":
    main()
