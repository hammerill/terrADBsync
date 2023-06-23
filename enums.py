from enum import Enum
import os

class Path(Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    ANDROID = "Android"

    def get_terraria_root_dir(self):
        if self == Path.WINDOWS:
            return os.path.join(os.environ["UserProfile"], "Documents", "My Games", "Terraria")
        elif self == Path.LINUX:
            return "~/.local/share/Terraria"
        elif self == Path.ANDROID:
            return "sdcard/Android/data/com.and.games505.TerrariaPaid"
        
    def get_terraria_players_dir(self):
        if self == Path.WINDOWS:
            return os.path.join(Path.WINDOWS.get_terraria_root_dir(), "Players")
        elif self == Path.LINUX:
            return f"{Path.LINUX.get_terraria_root_dir()}/Players"
        elif self == Path.ANDROID:
            return f"{Path.ANDROID.get_terraria_root_dir()}/Players"

    def get_terraria_worlds_dir(self):
        if self == Path.WINDOWS:
            return os.path.join(Path.WINDOWS.get_terraria_root_dir(), "Worlds")
        elif self == Path.LINUX:
            return f"{Path.LINUX.get_terraria_root_dir()}/Worlds"
        elif self == Path.ANDROID:
            return f"{Path.ANDROID.get_terraria_root_dir()}/Worlds"
        
    def get_terraria_array_dir(self):
        if self == Path.WINDOWS:
            return [os.path.join(Path.WINDOWS.get_terraria_players_dir()), 
                    os.path.join(Path.WINDOWS.get_terraria_worlds_dir())]
        elif self == Path.LINUX:
            return [os.path.join(Path.LINUX.get_terraria_players_dir()), 
                    os.path.join(Path.LINUX.get_terraria_worlds_dir())]
        elif self == Path.ANDROID:
            return [os.path.join(Path.ANDROID.get_terraria_players_dir()), 
                    os.path.join(Path.ANDROID.get_terraria_worlds_dir())]
    
    def get_terraria_backup_root_dir(self):
        if self == Path.WINDOWS:
            return os.path.join(Path.WINDOWS.get_terraria_root_dir(), "backups")
        elif self == Path.LINUX:
            return f"{Path.LINUX.get_terraria_root_dir()}/backups"
        elif self == Path.ANDROID:
            return f"{Path.ANDROID.get_terraria_root_dir()}/backups"