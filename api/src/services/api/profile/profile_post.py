from flask import jsonify
from sqlalchemy.exc import IntegrityError
from src.services.errors.error_handling import handle_error
from src.model.model_profile import ProfileModel
from src.schemas.schema_profile import profile_schema
from src.model import db

class ProfilePostService:
    @staticmethod
    def create_profile(profile_data):
        try:
            existing_document = ProfileModel.query.filter_by(document=profile_data['document']).first()
            if existing_document:
                return handle_error("Document already exists", 400)

            profile = profile_schema.load(data=profile_data)

            db.session.add(profile)
            db.session.commit()

            new_profile = profile_schema.dump(profile)
            return jsonify(data=new_profile), 201
        except IntegrityError as e:
            db.session.rollback()
            return handle_error(f"Error creating the profile", 400)
        except Exception as e:
            db.session.rollback()
            print("Error", e)
            return handle_error(f"Internal Server Error: {e}", 500)
