import request from 'supertest';
import app from '../index';

describe('API Health Check', () => {
  it('should return 200 on /health endpoint', async () => {
    const response = await request(app).get('/health');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('status', 'ok');
  });
});

describe('Auth Endpoints', () => {
  it('should return 400 if email or password is missing', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'test@test.com' });
    
    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error');
  });

  it('should return 401 for invalid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'invalid@test.com', password: 'wrongpassword' });
    
    expect(response.status).toBe(401);
  });
});

describe('Protected Endpoints', () => {
  it('should return 401 when accessing /api/children without token', async () => {
    const response = await request(app).get('/api/children');
    expect(response.status).toBe(401);
  });

  it('should return 401 when accessing /api/sessions without token', async () => {
    const response = await request(app).get('/api/sessions');
    expect(response.status).toBe(401);
  });
});
