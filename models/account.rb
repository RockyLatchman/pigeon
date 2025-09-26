
class Account < ActiveRecord::Base
  has_many :messages
  has_many :contacts

  def create_account
  end

  def update_account()
  end

  def deactivate_account()
  end

  def register()
  end

  def login()
  end

  def logout()
  end

  private

  def check_for_existence(account_existence)
  end

end
