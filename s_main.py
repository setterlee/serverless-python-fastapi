import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='setterlee',
    application_name='serverless-python-fastapi',
    app_uid='qGrb61RMkSRLqMZ2dm',
    org_uid='Mt5l92cZKXLK2yYPyh',
    deployment_uid='15761388-3d7e-4078-ab2e-5d4d7d25ee32',
    service_name='serverless-python-fastapi',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='4.1.0',
    disable_frameworks_instrumentation=False
)
handler_wrapper_kwargs = {'function_name': 'serverless-python-fastapi-dev-main', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('src/main.handler')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
