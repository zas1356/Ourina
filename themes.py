# ╔══════════════════════════════════════════════════════════════╗
# ║                      OURINA THEMES                            ║
# ║           Silakan edit atau tambah tema baru                  ║
# ╚══════════════════════════════════════════════════════════════╝

THEMES = {
    "dark": {
        "name": "🌙 Dark",
        "primary": "#9D4EDD",
        "secondary": "#7B2CBF",
        "accent": "#E0AAFF",
        "user": "#00D9FF",
        "assistant": "#C77DFF",
        "success": "#00FF88",
        "error": "#FF6B6B",
        "warning": "#FFE66D",
        "gradient": ["#9D4EDD", "#C77DFF", "#E0AAFF"],
    },
    "light": {
        "name": "☀️ Light",
        "primary": "#6B21A8",
        "secondary": "#7C3AED",
        "accent": "#A78BFA",
        "user": "#0891B2",
        "assistant": "#7C3AED",
        "success": "#059669",
        "error": "#DC2626",
        "warning": "#D97706",
        "gradient": ["#6B21A8", "#7C3AED", "#A78BFA"],
    },
    "ocean": {
        "name": "🌊 Ocean",
        "primary": "#0077B6",
        "secondary": "#00B4D8",
        "accent": "#90E0EF",
        "user": "#48CAE4",
        "assistant": "#00B4D8",
        "success": "#06D6A0",
        "error": "#EF476F",
        "warning": "#FFD166",
        "gradient": ["#03045E", "#0077B6", "#00B4D8"],
    },
    "sakura": {
        "name": "🌸 Sakura",
        "primary": "#FF69B4",
        "secondary": "#FFB6C1",
        "accent": "#FFC0CB",
        "user": "#FF1493",
        "assistant": "#FF69B4",
        "success": "#98FB98",
        "error": "#FF6347",
        "warning": "#FFD700",
        "gradient": ["#FF69B4", "#FFB6C1", "#FFC0CB"],
    },
    "forest": {
        "name": "🌲 Forest",
        "primary": "#228B22",
        "secondary": "#32CD32",
        "accent": "#90EE90",
        "user": "#00FA9A",
        "assistant": "#32CD32",
        "success": "#00FF7F",
        "error": "#FF4500",
        "warning": "#FFD700",
        "gradient": ["#228B22", "#32CD32", "#90EE90"],
    },
    "cyberpunk": {
        "name": "🤖 Cyberpunk",
        "primary": "#FF00FF",
        "secondary": "#00FFFF",
        "accent": "#FFFF00",
        "user": "#00FFFF",
        "assistant": "#FF00FF",
        "success": "#00FF00",
        "error": "#FF0000",
        "warning": "#FFFF00",
        "gradient": ["#FF00FF", "#00FFFF", "#FFFF00"],
    },
    
    # ─────────────────────────────────────────────────────────────
    # TAMBAH TEMA KUSTOM DI BAWAH INI
    # ─────────────────────────────────────────────────────────────
    # "mytheme": {
    #     "name": "🎨 My Theme",
    #     "primary": "#FFFFFF",
    #     "secondary": "#CCCCCC",
    #     "accent": "#888888",
    #     "user": "#00FF00",
    #     "assistant": "#FF00FF",
    #     "success": "#00FF00",
    #     "error": "#FF0000",
    #     "warning": "#FFFF00",
    #     "gradient": ["#FFFFFF", "#CCCCCC", "#888888"],
    # },
}

# ─────────────────────────────────────────────────────────────────
# THEME MANAGER (jangan edit bagian ini)
# ─────────────────────────────────────────────────────────────────
try:
    from config import DEFAULT_THEME
    current_theme = DEFAULT_THEME if DEFAULT_THEME in THEMES else "dark"
except:
    current_theme = "dark"


def get_theme():
    return THEMES.get(current_theme, THEMES["dark"])


def set_theme(theme_name):
    global current_theme
    if theme_name in THEMES:
        current_theme = theme_name
        return True
    return False


def list_themes():
    return list(THEMES.keys())
