from flask_restx import Resource,Namespace,fields
from flask_jwt_extended import jwt_required
from ..models.orders import Order
from http import HTTPStatus

order_namespace=Namespace('order', description='Namespace for orders')

order_model = order_namespace.model(
    'Order',{
        'id':fields.Integer(description="An ID"),
        'size':fields.String(description="Size of order",required=True,
            enum=['SMALL','MEDIUM','LARGE','EXTRA_LARGE']
        ),
        'order_status':fields.String(description="The status of the Order",
            required=True, enum=['PENDING','IN_TRANSIT','DELIVERED']
        )
    }
)
@order_namespace.route('/orders')
class OrderGetCreate(Resource):
    
    @order_namespace.marshal_with(order_model)
    def get(self):
        """
            Get all orders
        """
        orders=Order.query.all()
        return orders, HTTPStatus.OK
    
    @jwt_required
    def post(self):
        """
            Place an order
        """
        pass

@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

    def get(self, order_id):
        """
            Retrieve an order by id
        """
        pass

    def put(self, order_id):
        """
            Update an order by id
        """
        pass

    def delete(self, order_id):
        """
            Delete an order by id
        """
        pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self, user_id, order_id):
        """
            Get a user's specific order
        """
        pass

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):

    def get(self, user_id):
        """
            Get all orders by a specific user
        """
        pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

    def patch(self, order_id):
        """
            Update an order's status
        """
        pass