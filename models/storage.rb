

class Storage < ActiveRecord::Base
  belongs_to :account

  def upgrade_storage()
  end

  def retrieve_files()
  end

  def edit_file()
  end

  def add_file()
  end

  def remove_file()
  end

end
