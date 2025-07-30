import time
import logging

logger = logging.getLogger(__name__)

class RequestTimerMiddleware:
    def __init__(self, get_response):
        print("before_init_")
        self.get_response = get_response
        print("after_init_")

    def __call__(self, request):
        print("before_call_")
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        logger.info("Request %s %s completed in %.3fs",
                    request.method, request.path, duration)
        print("after_call_")
        return response

def request_timer(get_response):
    print("[request_timer] factory init")
    def middleware(request):
        print("[request_timer] before view", request.path)
        response = get_response(request)
        print("[request_timer] after view")
        return response
    return middleware
