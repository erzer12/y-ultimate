import React from 'react';
import { motion } from 'framer-motion';
import { Trophy, Calendar, MapPin, Users, Award, Clock, TrendingUp } from 'lucide-react';

const TournamentCard = ({ tournament, index }) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.5, delay: index * 0.1 }}
    className="bg-white rounded-2xl p-6 shadow-soft hover:shadow-lg transition-all duration-300"
  >
    <div className="flex items-start justify-between mb-4">
      <div className="flex-1">
        <h3 className="text-2xl font-headline font-bold text-gray-800 mb-2">
          {tournament.name}
        </h3>
        <p className="text-gray-600 mb-3">{tournament.description}</p>
      </div>
      <div className={`px-4 py-2 rounded-full text-sm font-semibold ${
        tournament.status === 'upcoming' 
          ? 'bg-accent-100 text-accent-700' 
          : tournament.status === 'live'
          ? 'bg-green-100 text-green-700'
          : 'bg-gray-100 text-gray-700'
      }`}>
        {tournament.status === 'upcoming' ? '🔜 Upcoming' : tournament.status === 'live' ? '🔴 Live' : '✅ Completed'}
      </div>
    </div>

    <div className="grid grid-cols-2 gap-4 mb-4">
      <div className="flex items-center text-gray-600">
        <Calendar className="w-5 h-5 mr-2 text-primary-500" />
        <span className="text-sm">{tournament.date}</span>
      </div>
      <div className="flex items-center text-gray-600">
        <MapPin className="w-5 h-5 mr-2 text-secondary-500" />
        <span className="text-sm">{tournament.location}</span>
      </div>
      <div className="flex items-center text-gray-600">
        <Users className="w-5 h-5 mr-2 text-accent-500" />
        <span className="text-sm">{tournament.teams} Teams</span>
      </div>
      <div className="flex items-center text-gray-600">
        <Trophy className="w-5 h-5 mr-2 text-yellow-500" />
        <span className="text-sm">{tournament.division}</span>
      </div>
    </div>

    {tournament.status === 'live' && tournament.liveMatches && (
      <div className="border-t pt-4 mt-4">
        <h4 className="font-semibold text-gray-700 mb-3 flex items-center">
          <Clock className="w-4 h-4 mr-2 text-green-500" />
          Live Matches
        </h4>
        {tournament.liveMatches.map((match, idx) => (
          <div key={idx} className="bg-gray-50 rounded-lg p-3 mb-2 flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center justify-between text-sm">
                <span className="font-medium">{match.team1}</span>
                <span className="text-2xl font-bold text-primary-600 mx-4">{match.score1}</span>
              </div>
              <div className="flex items-center justify-between text-sm mt-1">
                <span className="font-medium">{match.team2}</span>
                <span className="text-2xl font-bold text-secondary-600 mx-4">{match.score2}</span>
              </div>
            </div>
            <div className="text-xs text-gray-500 ml-4">
              <div>Field {match.field}</div>
              <div className="text-green-600 font-semibold">●  LIVE</div>
            </div>
          </div>
        ))}
      </div>
    )}

    {tournament.status === 'upcoming' && (
      <div className="mt-4">
        <button className="w-full bg-primary-500 hover:bg-primary-600 text-white font-semibold py-3 rounded-xl transition-colors duration-200">
          View Details & Register
        </button>
      </div>
    )}

    {tournament.status === 'completed' && tournament.winner && (
      <div className="border-t pt-4 mt-4">
        <div className="flex items-center justify-center bg-yellow-50 rounded-lg p-4">
          <Award className="w-6 h-6 text-yellow-600 mr-3" />
          <div>
            <div className="text-sm text-gray-600">Tournament Winner</div>
            <div className="font-bold text-gray-800">{tournament.winner}</div>
          </div>
        </div>
      </div>
    )}
  </motion.div>
);

const Tournament = () => {
  // Mock data - In production, this would come from the API
  const tournaments = [
    {
      name: "Spring Ultimate Cup 2024",
      description: "Annual youth tournament bringing together teams from across Johannesburg",
      date: "March 15-17, 2024",
      location: "Wanderers Stadium, JHB",
      teams: 16,
      division: "U15 Mixed",
      status: "live",
      liveMatches: [
        { team1: "Phoenix Rising", team2: "Thunder Strikers", score1: 12, score2: 10, field: "1" },
        { team1: "Coastal Warriors", team2: "Valley Hawks", score1: 8, score2: 11, field: "2" },
      ]
    },
    {
      name: "Community Championship",
      description: "Community-based teams competing for the championship title",
      date: "April 5-7, 2024",
      location: "Alexandra Sports Complex",
      teams: 12,
      division: "U18 Open",
      status: "upcoming"
    },
    {
      name: "Winter Youth Series",
      description: "Development tournament for emerging young players",
      date: "May 20-22, 2024",
      location: "Soweto Community Grounds",
      teams: 10,
      division: "U12 Mixed",
      status: "upcoming"
    },
    {
      name: "Summer Showcase 2023",
      description: "End-of-year tournament featuring the best teams",
      date: "December 10-12, 2023",
      location: "Pretoria Sports Arena",
      teams: 14,
      division: "U15 Mixed",
      status: "completed",
      winner: "Township Titans"
    }
  ];

  const upcomingTournaments = tournaments.filter(t => t.status === 'upcoming');
  const liveTournaments = tournaments.filter(t => t.status === 'live');
  const completedTournaments = tournaments.filter(t => t.status === 'completed');

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-primary-500 to-secondary-500 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-center"
          >
            <Trophy className="w-16 h-16 mx-auto mb-4" />
            <h1 className="text-5xl font-headline font-bold mb-4">
              Y-Ultimate Tournaments
            </h1>
            <p className="text-xl opacity-90 max-w-2xl mx-auto">
              Experience the spirit of Ultimate Frisbee through competitive tournaments
              that build character, teamwork, and community
            </p>
          </motion.div>
        </div>
      </div>

      {/* Stats Overview */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-2xl p-6 shadow-soft text-center"
          >
            <Trophy className="w-8 h-8 text-yellow-500 mx-auto mb-2" />
            <div className="text-3xl font-bold text-gray-800">24</div>
            <div className="text-sm text-gray-600">Tournaments This Year</div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-2xl p-6 shadow-soft text-center"
          >
            <Users className="w-8 h-8 text-primary-500 mx-auto mb-2" />
            <div className="text-3xl font-bold text-gray-800">340</div>
            <div className="text-sm text-gray-600">Teams Participated</div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="bg-white rounded-2xl p-6 shadow-soft text-center"
          >
            <Award className="w-8 h-8 text-accent-500 mx-auto mb-2" />
            <div className="text-3xl font-bold text-gray-800">1,200+</div>
            <div className="text-sm text-gray-600">Young Athletes</div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="bg-white rounded-2xl p-6 shadow-soft text-center"
          >
            <TrendingUp className="w-8 h-8 text-secondary-500 mx-auto mb-2" />
            <div className="text-3xl font-bold text-gray-800">95%</div>
            <div className="text-sm text-gray-600">Spirit Score Average</div>
          </motion.div>
        </div>
      </div>

      {/* Live Tournaments */}
      {liveTournaments.length > 0 && (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.6 }}
          >
            <h2 className="text-3xl font-headline font-bold text-gray-800 mb-6 flex items-center">
              <span className="w-3 h-3 bg-green-500 rounded-full mr-3 animate-pulse"></span>
              Live Now
            </h2>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {liveTournaments.map((tournament, index) => (
                <TournamentCard key={index} tournament={tournament} index={index} />
              ))}
            </div>
          </motion.div>
        </div>
      )}

      {/* Upcoming Tournaments */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.7 }}
        >
          <h2 className="text-3xl font-headline font-bold text-gray-800 mb-6">
            Upcoming Tournaments
          </h2>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {upcomingTournaments.map((tournament, index) => (
              <TournamentCard key={index} tournament={tournament} index={index} />
            ))}
          </div>
        </motion.div>
      </div>

      {/* Past Tournaments */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          <h2 className="text-3xl font-headline font-bold text-gray-800 mb-6">
            Past Tournaments
          </h2>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {completedTournaments.map((tournament, index) => (
              <TournamentCard key={index} tournament={tournament} index={index} />
            ))}
          </div>
        </motion.div>
      </div>

      {/* CTA Section */}
      <div className="bg-gradient-to-r from-primary-500 to-secondary-500 text-white py-16 mt-12">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <h2 className="text-4xl font-headline font-bold mb-4">
            Want to Participate?
          </h2>
          <p className="text-xl mb-8 opacity-90">
            Register your team for upcoming tournaments and be part of the Y-Ultimate community
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button className="bg-white text-primary-600 hover:bg-gray-100 font-semibold px-8 py-4 rounded-xl transition-colors duration-200">
              Register Your Team
            </button>
            <button className="bg-transparent border-2 border-white hover:bg-white hover:text-primary-600 font-semibold px-8 py-4 rounded-xl transition-colors duration-200">
              Learn More
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Tournament;
