from flask_bcrypt import Bcrypt
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from src.services.errors.error_handling import handle_error
from src.schemas.schema_user import user_schema
from src.model import db
from src.model.model_user import UserModel

bcrypt = Bcrypt()
class UserPostService:
    @staticmethod
    def create_user(user_data):
        try:
            # Verificar si el usuario ya existe
            existing_user = UserModel.query.filter_by(username=user_data['username']).first()
            if existing_user:
                return handle_error("User already exists", 400)

            # Crear un nuevo usuario
            user = user_schema.load(data=user_data)
            user.set_category()

            hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
            user.password = hashed_password

            db.session.add(user)
            db.session.commit()

            new_user = user_schema.dump(user)
            return jsonify(data=new_user), 201

        except IntegrityError as e:
            db.session.rollback()  # Deshacer los cambios pendientes en la transacción
            return handle_error(f"Error al crear el usuario", 400)
        except Exception as e:
            db.session.rollback()  # Deshacer los cambios pendientes en la transacción
            return handle_error(f"Internal Server Error", 500)
       