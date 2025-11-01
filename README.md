
# Y-Ultimate Management Platform

A unified web platform to manage Y-Ultimate's tournaments and coaching programs, built with FastAPI, React, and PostgreSQL.

![Y-Ultimate](https://img.shields.io/badge/Status-Active-success)
![Node](https://img.shields.io/badge/Node-v20+-green)
![Python](https://img.shields.io/badge/Python-3.12+-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🎯 Project Overview

**Y-Ultimate** is a non-profit organization that teaches life skills to children from under-resourced communities using the sport of Ultimate Frisbee. This platform digitizes, centralizes, and visualizes all operations for both Coaching Programmes and Tournaments.

### ✨ Key Features

**Coaching Programme Management**
- 👥 Unified child profiles with dual-program support
- 📊 Real-time attendance tracking
- 🏫 Session management for coaches
- 🏠 Home visit tracking
- 📈 LSAS (Life Skills Assessment System) with progress tracking
- 📑 Automated reporting and analytics

**Tournament Management**
- 🏆 Tournament creation and management
- 👕 Player and team registration with approval workflows
- 📅 Match scheduling and bracket generation
- 🎯 Live scoring and spirit score tracking
- 🏅 Automatic leaderboards and standings

**User Roles**
- Programme Director/Admin (Full Access)
- Programme Manager (Management)
- Coach/Facilitator (Session & Assessment)
- Reporting/Data Team (Analytics)
- Community/School Coordinator (Site-Level)

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** (recommended)
- **Node.js v20+** for frontend development
- **Python 3.12+** for backend development
- **PostgreSQL 15+**

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/erzer12/y-ultimate.git
cd y-ultimate
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start with Docker Compose** (Recommended)
```bash
docker compose up -d --build
```

The application will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Default Login Credentials
```
Email: admin@yultimate.org
Password: password123
```

## 📚 Documentation

- **[Setup Guide](SETUP.md)** - Detailed installation and configuration
- **[Data Model](DATA_MODEL.md)** - Database schema and relationships
- **[Contributing](CONTRIBUTING.md)** - How to contribute to the project
- **[API Reference](http://localhost:8000/docs)** - Interactive API documentation

## 🛠️ Technology Stack

**Backend**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- JWT Authentication
- Pydantic (Data validation)

**Frontend**
- React 19 with Vite
- TailwindCSS (Styling)
- Framer Motion (Animations)
- React Query (Data fetching)
- Lucide React (Icons)
- Recharts (Data visualization)

**DevOps**
- Docker & Docker Compose
- Automated CI/CD ready

## 🎨 Design Theme: "Play, Purpose, and Progress"

The platform features a vibrant, energetic design reflecting the spirit of Ultimate Frisbee:

- **Colors**: Bright blues and greens (primary), orange/yellow (accents)
- **Typography**: Poppins/Montserrat (headlines), Inter (body)
- **Style**: Modern flat design with soft shadows and rounded edges
- **Animation**: Parallax hero section with interactive elements

## 🗂️ Project Structure

```
y-ultimate/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── core/           # Core configuration
│   │   └── db/             # Database setup
│   ├── scripts/            # Utility scripts
│   └── requirements.txt    # Python dependencies
├── frontend/                # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   └── assets/         # Static assets
│   └── package.json        # Node dependencies
├── docker-compose.yaml      # Docker configuration
└── docs/                    # Additional documentation
```

## 🧪 Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Seed Mock Data
```bash
cd backend
python scripts/seed_data.py
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Y-Ultimate organization and its dedicated coaches
- All contributors and supporters
- The Ultimate Frisbee community

## 📞 Support

For issues and questions:
- **GitHub Issues**: [Create an issue](https://github.com/erzer12/y-ultimate/issues)
- **Documentation**: See `/docs` folder

---

**Built with ❤️ for the Y-Ultimate community** 🏐
