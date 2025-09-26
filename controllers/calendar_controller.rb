
class CalendarController < ApplicationController
   get '/' do
     erb :calendar
   end

   post '/add-event/:event' do
   end

   put '/edit-event/:event_id' do
   end

   delete '/remove-item/:event_id' do
   end
end
