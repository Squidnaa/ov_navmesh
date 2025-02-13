import omni.ui as ui
from .styles import NavGuiStyles

CustomStyles = NavGuiStyles()

class NavWindow:
    def __init__(self):
    
        self._nav_window = ui.Window("NavMesh", width=300, height=600, visible=True,
                                     flags = ui.WINDOW_FLAGS_NO_TITLE_BAR | ui.WINDOW_FLAGS_NO_COLLAPSE | ui.WINDOW_FLAGS_NO_RESIZE)
        
        with self._nav_window.frame:
            with ui.VStack(height=0, spacing=5):
                # these buttons need clicked functions. as well as decisions on where
                # they are going to be placed. But for now ill keep them here.
                self.assign_btn = ui.Button("Assign Mesh", style=CustomStyles.solid_yellow_button)
                self.bld_btn = ui.Button("Build NavMesh", style=CustomStyles.solid_red_button)
                self.rnd_pnts_btn = ui.Button("Get Random Points", style=CustomStyles.solid_red_button)
                self.rnd_pth_btn = ui.Button("Get Random Path", style=CustomStyles.solid_red_button)
                self.mesh_btn = ui.Button("Get Mesh", style=CustomStyles.solid_red_button)
                self.getout_btn = ui.Button("Get Out", style=CustomStyles.solid_red_button)
                self.mke_out_btn = ui.Button("Make Out", style=CustomStyles.solid_red_button)
                self.bld_wall_btn = ui.Button("Build Wall", style=CustomStyles.solid_red_button)
                self.make_wall_btn = ui.Button("Make Wall", style=CustomStyles.solid_red_button)