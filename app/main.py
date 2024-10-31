from flask import Flask
from graphene import Schema
from app.gql.query import Query
from flask_graphql import GraphQLView


app = Flask(__name__)

schema = Schema(query=Query)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run()
