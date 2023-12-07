from rest_framework import routers
from .views import *

api_router = routers.SimpleRouter()
api_router.register(r'deposits', DepositAPIViewSet)
api_router.register(r'operations', OperationAPIViewSet)
api_router.register(r'categories', CategoryAPIViewSet)
api_router.register(r'types', CategoryTypeAPIViewSet)
api_router.register(r'debts', DebtAPIViewSet)