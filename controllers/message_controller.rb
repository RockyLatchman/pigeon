require_relative './application_controller'
require_relative '../models/message'

class MessageController < ApplicationController
   get '/:id' do
     #inbox = Message.new
     # @messages = inbox.receive_messages(params[:id])
     #erb :inbox
   end


end
