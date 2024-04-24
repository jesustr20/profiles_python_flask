from flask import Blueprint, request, jsonify
from src.services.errors.error_handling import handle_error
from src.schemas.schema_profile import profile_schema
from src.services.api.profile.profile_post import ProfilePostService
from src.services.api.profile.profile_get import ProfileGetService
from src.services.api.profile.profile_by_id_get import ProfileIdGetService
from src.services.api.profile.profile_update import ProfileIdUpdateService
from src.services.api.profile.profile_delete import ProfileDeleteService

api_pf_bp = Blueprint('api_profiles', __name__)

#Create a New Profile
@api_pf_bp.route('/profiles', methods=['POST'])
def create_profile():
    profile_data = request.json
    return ProfilePostService.create_profile(profile_data)

#Get all profiles
@api_pf_bp.route('/profiles', methods=['GET'])
def get_profiles():
    profiles_data = request
    return ProfileGetService.get_profiles(profiles_data)

#Get profile by id
@api_pf_bp.route('/profiles/<int:id>', methods=['GET'])
def get_profile_by_id(id):
    return ProfileIdGetService.get_profile_by_id(id)

#Update profile by id
@api_pf_bp.route('/profiles/<int:id>', methods=['PATCH'])
def update_profile_by_id(id):
    return ProfileIdUpdateService.update_profile_by_id(id, request.json)

#Delete profile by id
@api_pf_bp.route('/profiles/<int:id>', methods=['DELETE'])
def delete_profile_by_id(id):
    return ProfileDeleteService.delete_profile_by_id(id)