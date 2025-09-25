

class Message < ActiveRecord::Base

  def receive_messages
    Message.all
  end
end
