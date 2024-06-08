class PrintRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('\033[32m' + f'Request: {request.method} {request.path}' + '\033[0m')
        print('\033[32m' + 'Headers:' + '\033[0m')
        for header, value in request.META.items():
            if header.startswith('HTTP_'):
                print('\033[32m' + f'{header}: {value}' + '\033[0m')

        if request.body:
            print('\033[32m' + 'Body:' + '\033[0m')
            print('\033[32m' + str(request.body) + '\033[0m')

        response = self.get_response(request)
        return response