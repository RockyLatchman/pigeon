require_relative './application_controller'
require_relative '../models/message'

class MessageController < ApplicationController
   get '/' do
     erb :inbox
   end


end
