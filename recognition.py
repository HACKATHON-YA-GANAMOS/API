
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
    headers = {'Authorization':'Bearer ' + "DXIN2GTRZWGIF2A2SJOZVGIO3B5MKE7H5723AN4YDGOQMWMTPKRKHE32747ACOGBX4VIEPCQZ5OKCJYB6JNZQNJCDBAKEPIXTVTDOBI", 'Cache-Control': 'no-cache'}
    return _prediction_request("https://api.einstein.ai/v2/vision/predict", payload, headers)
