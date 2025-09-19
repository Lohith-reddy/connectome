#!/usr/bin/env python3
"""
Brain Connectivity System Startup Script
"""

import sys
from pathlib import Path

def main():
    """Main startup function"""
    print("🧠 Brain Connectivity System v2.0")
    print("=" * 50)

    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9+ required")
        sys.exit(1)

    # Check if in correct directory
    if not Path("pyproject.toml").exists():
        print("❌ Run from brain-connectivity-system directory")
        sys.exit(1)

    # Check environment file
    if not Path(".env").exists():
        print("⚠️ .env file not found. Creating from .env.example...")
        if Path(".env.example").exists():
            import shutil
            shutil.copy(".env.example", ".env")
            print("✅ .env file created. Please configure your API keys.")
        else:
            print("❌ .env.example not found")

    try:
        print("🚀 Starting Brain Connectivity System...")
        print("📊 Main interface: http://localhost:8000")
        print("👑 Admin interface: http://localhost:8000/admin") 
        print("🔍 Workflow viewer: http://localhost:8000/workflow")
        print("📚 API docs: http://localhost:8000/docs")
        print()
        print("Press Ctrl+C to stop")

        from brain_connectivity import main as app_main
        app_main()

    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("Install with: poetry install")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
