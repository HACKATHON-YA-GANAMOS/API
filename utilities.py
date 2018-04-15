from cloudinary import uploader, config
import json

config(
  cloud_name = "dnta2siwa",
  api_key = "397785724294295",
  api_secret = "wDpM-7o__ho8OUdR2fJp8Mp6i7E"
)


def get_image_url(image_path):
    # Se pueden obtener más datos de la imagen subida si se quiere
    data = uploader.upload(image_path)
    return data["url"]

def jsonToDict(path):
	with open(path, encoding="utf-8") as json_file:
	    json_str = json_file.read()
	    json_data = json.loads(json_str)

	return json_data


def dictToJson(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=3)