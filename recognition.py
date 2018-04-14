
import requests
def _prediction_request(url, payload, headers):
    """Make a prediction request.
    Args:
        url: endpoint url
        data: multipart payload
        headers: request headers
    Returns:
        JSON response
    """    
    try:        
        response = requests.post(url, files=payload, headers=headers)
        return response
    except requests.exceptions.RequestException as exp:
        raise exp("Prediction failed: \"{}\"".format(response))
def predict_with_url(image_url):
    """Run a prediction against a model using image url.
    Args:
        token: oauth token
        model_id: model id
        image_url: image url
    Returns:
        A json string containing classes and probabilities.
    """
    
    payload = {'sampleLocation': (None, image_url), 'modelId': (None, 'FoodImageClassifier')}
    headers = {'Authorization':'Bearer ' + "3A5BPUODR3JF7XQPVSF3L7O6ZPYURZMMAE7T4BH7IEMEL67WKE5B6S5FXJ3PTZQKXCIMF2CCGXXSYFZOIWCQGU52LEQAE3ZYOPGYFGY", 'Cache-Control': 'no-cache'}
    return _prediction_request("https://api.einstein.ai/v2/vision/predict", payload, headers)
