from flask import escape
import functions_framework
# import pprint
import google.generativeai as palm

palm.configure(api_key='YOUR API KEY')

@functions_framework.http
def palm_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'prompt' in request_json:
        prompt = request_json['prompt']
    elif request_args and 'prompt' in request_args:
        prompt = request_args['prompt']
    else:
        return 'No prompt provided'
    if prompt == '':
        return 'Empty prompt provided'
    
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    # print(model)
    completion = palm.generate_text(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )

    if (request_json and 'prompt' in request_json) or (request_args and 'prompt' in request_args):
        if completion.result in [None, '']:
            return 'Empty completion result'
        return completion.result
    else:
        return 'No prompt provided'
