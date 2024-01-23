def TestCustomMiddleware(get_response):
    def middleware(request):
        # 요청 전처리 코드
        print(f"Request URL: {request.path}")

        response = get_response(request)

        #응답 후처리 코드
        print(f"Response status code:{response.status_code}")

        return response
    return middleware
