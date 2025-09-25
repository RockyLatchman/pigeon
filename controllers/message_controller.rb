require_relative './application_controller'
require_relative '../models/message'

class MessageController < ApplicationController
   get '/' do
     inbox = Message.new
     @messages = inbox.receive_messages
     erb :inbox
   end

end
