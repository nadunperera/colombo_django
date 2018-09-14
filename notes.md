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


- UserStatus Model in User Service?
-- UserStatus Model
--- user
--- status
----- new
----- in_progress
----- delayed_progress
----- service_not_suitable

- Needs to have a Reminder Service where Colombo reminds particular users about upcoming activities
-- Reminder Model
--- reminder_date
--- reminder

- UserConnection Model
--- user_child
--- user_master
--- connection_type
----- referrer
----- business_partner
--- created_at
--- updated_at
