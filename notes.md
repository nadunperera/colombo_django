# CERTAIN SECTION

- UserStatus Model in User Service?
- Looks like this needs to be in the UserModel, so we can filter users with their status
-- UserStatus Model
--- user
--- status
----- staff
----- new_client
----- in_progress
----- delayed_progress
----- service_not_suitable

- Follow up date for Users needs to be included in the user_activity service
-- Is this a user_activity service?
-- UserActivity Model
--- user
--- activity_type
----- initial_contact
----- first_meeting
----- second_meeting
----- eoi_related
----- other
--- notes
--- created_at
--- updated_at

- How about a Meeting Service
-- Meeting Model
--- user
--- meeting_type
----- first_meeting
----- second_meeting
----- other
--- meeting_outcome
----- success
----- failed
----- neutral
--- notes
--- created_at
--- updated_at

- Needs to have a Follow Up Service where Colombo reminds particular users about upcoming activities
- This needs to be a part of the Meeting Service. A Follow Up Model
-- FollowUp Model
--- follow_up_date
--- description

# UNCERTAIN SECTION

- UserConnection Model
--- user_child
--- user_master
--- connection_type
----- referrer
----- business_partner
--- created_at
--- updated_at

- EOI Model
--- user
----- property
----- lot
----- sales_agent
----- second_sales_agent
