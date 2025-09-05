# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
import colors
mod = "mod4"
terminal = guess_terminal()
colors = colors.DoomOne

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen(home,start_new_session=True)


def init_widgets_list():
    widgets_list = [
        widget.Spacer(length = 8),
        widget.Prompt(
                 font = "Fira Mono",
                 fontsize=14,
                 foreground = colors[1]
        ),
        widget.GroupBox(
                 fontsize = 11,
                 margin_y = 5,
                 margin_x = 14,
                 padding_y = 0,
                 padding_x = 2,
                 borderwidth = 3,
                 active = colors[8],
                 inactive = colors[9],
                 rounded = False,
                 highlight_color = colors[0],
                 highlight_method = "line",
                 this_current_screen_border = colors[7],
                 this_screen_border = colors [4],
                 other_current_screen_border = colors[7],
                 other_screen_border = colors[4],
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Fira Mono",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Fira Mono",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.CurrentLayout(
                 foreground = colors[1],
                 padding = 5
                 ),
        widget.TextBox(
                 text = '|',
                 font = "Fira Mono",
                 foreground = colors[9],
                 padding = 2,
                 fontsize = 14
                 ),
        widget.WindowName(
                 foreground = colors[6],
                 padding = 8,
                 max_chars = 40
                 ),

        widget.Backlight(
            backlight_name = 'intel_backlight',
            change_command = 'brightnessctl set {0}',
            format='☀ {percent:2.0%}',
            foreground = colors[5],
            padding = 8
        ),
        widget.Battery(
            # Display format: icon + percentage + time estimate
            format='{char} {percent:2.0%}',
            fmt = 'Bat: {}',
            # Custom icons for different states
            charge_char='^',    # Charging icon
            discharge_char='V', # Discharging icon
            full_char='F',      # Full battery icon
            empty_char='X',      # Empty battery icon
            unknown_char='?',    # Unknown state icon
    
    # Alert thresholds
            low_percentage=0.15,           # Consider low below 15%
            low_foreground='#ff0000',      # Red text when low
            notify_below=10,               # System notification below 10%
    
    # Visual settings
            foreground= colors[8],          # Light blue text
            padding=8,
            update_interval=1,            # Update every 15 seconds
)
,
        widget.Memory(
                 foreground = colors[8],
                 padding = 8, 
                 format = '{MemUsed: .0f}{mm}',
                 fmt = '🖥  Mem: {}',
                 ),
        widget.Volume(
                 foreground = colors[7],
                 padding = 8, 
                 fmt = '🕫  Vol: {}',
                 widget_name="volume",
                 step = 5,
                 ),
        widget.Clock(
                 foreground = colors[8],
                 padding = 8, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-date')},
                 ## Uncomment for date and time 
                 format = "⧗  %a, %b %d - %H:%M",
                 ## Uncomment for time only
                 ##format = "⧗  %I:%M %p",
                 ),
        widget.Systray(padding = 6),
        widget.Spacer(length = 8),

        ]
    return widgets_list


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "m", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod,"shift"], "c", lazy.window.kill(), desc="Kill focused window"),

#Use Cases
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #rofi spawning
    Key([mod], "r", lazy.spawn(["rofi","-show","drun"]), desc="run application"),
    Key([mod,"shift"], "r", lazy.spawn(["rofi","-show","run","-theme","nord"]), desc="run application"),
    Key([mod], "w", lazy.spawn(["rofi","-show","window", "-theme","nord"]), desc="show windows"),
    Key([mod,"shift"], 'q' ,lazy.spawn(os.path.expanduser("~/.config/qtile/quitmenu.sh")),desc="quitmenu"),
    #Volume
    Key([], "XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol()),
    Key([], "XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol()),
    Key([], "XF86AudioMute", lazy.widget["volume"].mute()),
    #Brightness
    Key([], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set 5%+"), 
        desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 5%-"), 
        desc="Decrease brightness"),
    
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layout_theme = {"border_width": 2,
                "margin": 12,
                "border_focus": colors[8],
                "border_normal": colors[0]
                }
layouts = [
    layout.Columns(**layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira Bold",
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(widgets=init_widgets_list(),margin=[8,12,0,12],size=30)
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
