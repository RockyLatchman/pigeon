

class Message < ActiveRecord::Base

  def receive_messages(recipient_id)
    Message.where(recipient_id: recipient_id)
  end
end
