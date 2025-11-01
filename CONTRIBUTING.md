# Contributing to Y-Ultimate Management Platform

Thank you for your interest in contributing to Y-Ultimate! This document provides guidelines and instructions for contributing to the project.

## 🌟 Ways to Contribute

- 🐛 **Report Bugs**: Submit detailed bug reports
- 💡 **Suggest Features**: Propose new features or improvements
- 📝 **Improve Documentation**: Help make our docs better
- 💻 **Write Code**: Submit pull requests for bug fixes or features
- 🧪 **Write Tests**: Improve test coverage
- 🎨 **Design**: Contribute UI/UX improvements

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/y-ultimate.git
cd y-ultimate

# Add upstream remote
git remote add upstream https://github.com/erzer12/y-ultimate.git
```

### 2. Create a Branch

```bash
# Create a descriptive branch name
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Set Up Development Environment

Follow the [Setup Guide](SETUP.md) to configure your local environment.

## 📋 Development Guidelines

### Code Style

#### Backend (Python/FastAPI)
- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Write docstrings for all public functions and classes
- Max line length: 100 characters

```python
def create_session(
    session: SessionCreate,
    db: Session = Depends(get_db)
) -> Session:
    """
    Create a new coaching session.
    
    Args:
        session: Session data to create
        db: Database session dependency
        
    Returns:
        Created session object
    """
    # Implementation
```

#### Frontend (React/JavaScript)
- Use functional components with hooks
- Follow Airbnb React style guide
- Use descriptive variable names
- Keep components small and focused
- Use Tailwind CSS classes for styling

```jsx
const ChildProfile = ({ childId }) => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['child', childId],
    queryFn: () => fetchChildProfile(childId)
  });

  if (isLoading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;

  return (
    <div className="p-6 bg-white rounded-2xl shadow-soft">
      {/* Component content */}
    </div>
  );
};
```

### Commit Messages

Use conventional commit format:

```
type(scope): brief description

Detailed explanation of what changed and why.

Fixes #123
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(api): add endpoint for bulk attendance marking

Implements POST /api/v1/attendance/bulk endpoint that allows
coaches to mark attendance for multiple children at once.

Closes #45
```

```
fix(frontend): resolve navigation menu overflow on mobile

The mobile navigation menu was cutting off on smaller screens.
Updated the CSS to use proper scrolling container.

Fixes #78
```

### Testing

#### Backend Tests
```bash
cd backend
pytest
pytest --cov=app tests/
```

Write tests for:
- All API endpoints
- Business logic functions
- Database models and relationships

Example:
```python
def test_create_child_profile(client, db):
    """Test creating a child profile"""
    response = client.post(
        "/api/v1/profiles/",
        json={
            "name": "John Doe",
            "date_of_birth": "2010-05-15",
            "school": "Test School"
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
```

#### Frontend Tests
```bash
cd frontend
npm test
```

### Documentation

- Update README.md if changing setup process
- Update API documentation for new endpoints
- Add JSDoc comments for complex functions
- Update FEATURE_WALKTHROUGH.md for new features

## 🔄 Pull Request Process

### 1. Before Submitting

- ✅ Code follows style guidelines
- ✅ All tests pass
- ✅ New tests added for new features
- ✅ Documentation updated
- ✅ Commit messages follow convention
- ✅ Branch is up to date with main

```bash
# Update your branch
git fetch upstream
git rebase upstream/main
```

### 2. Submit Pull Request

1. Push your branch to your fork
2. Go to the original repository
3. Click "New Pull Request"
4. Fill out the PR template completely
5. Link related issues

### 3. PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing performed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings generated
```

### 4. Review Process

- Maintainers will review your PR
- Address any requested changes
- Once approved, PR will be merged

## 🐛 Reporting Bugs

Use the GitHub issue template and include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Step-by-step instructions
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: OS, browser, Python/Node versions
6. **Screenshots**: If applicable
7. **Additional Context**: Any other relevant information

## 💡 Suggesting Features

Submit feature requests via GitHub issues:

1. **Problem Statement**: What problem does this solve?
2. **Proposed Solution**: How would you solve it?
3. **Alternatives**: Other solutions considered
4. **Benefits**: Who benefits and how?
5. **Additional Context**: Mockups, examples, etc.

## 📞 Communication

- **GitHub Issues**: Bug reports and feature requests
- **Pull Requests**: Code contributions
- **Discussions**: General questions and ideas

## 🏅 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in release notes
- Given credit in commit history

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## 🙏 Thank You!

Your contributions make Y-Ultimate better for everyone. Thank you for taking the time to contribute!

---

**Questions?** Open an issue or reach out to the maintainers.
