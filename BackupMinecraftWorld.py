from time import strftime
import shutil


def zipWorld(world):

	return shutil.make_archive(world+"_backup_"+strftime("%m_%d_%H_%M_%S"), 'zip', world)

	# with ZipFile(world+"_backup_"+strftime("%m_%d_%H_%M_%S")+".zip", 'w', zipfile.ZIP_DEFLATED) as zippedWorld:
	# 	for dirpath,dirnames,filenames in os.walk("/home/minecraft/"+world):
	# 		for filename in filenames:
	# 			zippedWorld.write(os.path.join(dirpath,filename))
	# return zippedWorld
		
def emailWorld(zippedWorld):
	# TODO


if __name__ == "__main__":

	for world in ['world', 'world_the_nether', 'world_the_end']:
		emailWorld(zipWorld(world))

