"""
AI Content Analyzer & Social Media Manager
A comprehensive Python project demonstrating:
- Data structures (lists, dictionaries, tuples)
- Loops and conditionals
- Functions and modular code
- File handling
- Real-world application (content analysis and management)
"""

import json
from datetime import datetime
from collections import Counter
import re

class ContentAnalyzer:
    """Analyzes text content for insights and metrics"""
    
    def __init__(self):
        self.stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'but', 'is', 'are', 'was', 'were'}
    
    def analyze_sentiment(self, text):
        """Analyze sentiment using keyword matching"""
        positive_words = ['great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'best', 'awesome', 'good', 'happy']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'worst', 'poor', 'disappointing', 'sad', 'angry']
        
        text_lower = text.lower()
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count > neg_count:
            return "Positive", pos_count - neg_count
        elif neg_count > pos_count:
            return "Negative", neg_count - pos_count
        else:
            return "Neutral", 0
    
    def extract_keywords(self, text, top_n=5):
        """Extract top keywords from text"""
        # Remove punctuation and convert to lowercase
        words = re.findall(r'\b\w+\b', text.lower())
        # Filter out stop words
        filtered_words = [w for w in words if w not in self.stop_words and len(w) > 3]
        # Count word frequency
        word_counts = Counter(filtered_words)
        return word_counts.most_common(top_n)
    
    def calculate_readability(self, text):
        """Calculate readability score (simplified)"""
        sentences = text.split('.')
        words = text.split()
        
        if len(sentences) == 0 or len(words) == 0:
            return 0
        
        avg_words_per_sentence = len(words) / len(sentences)
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        # Simple readability score
        score = 100 - (avg_words_per_sentence * 2) - (avg_word_length * 5)
        return max(0, min(100, score))

class SocialMediaPost:
    """Represents a social media post"""
    
    def __init__(self, platform, content, author, hashtags=None):
        self.platform = platform
        self.content = content
        self.author = author
        self.hashtags = hashtags if hashtags else []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.engagement = {'likes': 0, 'shares': 0, 'comments': 0}
    
    def add_engagement(self, likes=0, shares=0, comments=0):
        """Add engagement metrics"""
        self.engagement['likes'] += likes
        self.engagement['shares'] += shares
        self.engagement['comments'] += comments
    
    def get_engagement_rate(self):
        """Calculate total engagement"""
        return sum(self.engagement.values())
    
    def to_dict(self):
        """Convert post to dictionary"""
        return {
            'platform': self.platform,
            'content': self.content,
            'author': self.author,
            'hashtags': self.hashtags,
            'timestamp': self.timestamp,
            'engagement': self.engagement
        }

class SocialMediaManager:
    """Manages social media posts and analytics"""
    
    def __init__(self):
        self.posts = []
        self.analyzer = ContentAnalyzer()
    
    def create_post(self, platform, content, author, hashtags=None):
        """Create a new social media post"""
        post = SocialMediaPost(platform, content, author, hashtags)
        self.posts.append(post)
        print(f"✅ Post created on {platform} by {author}")
        return post
    
    def analyze_post(self, post):
        """Analyze a post for insights"""
        sentiment, score = self.analyzer.analyze_sentiment(post.content)
        keywords = self.analyzer.extract_keywords(post.content)
        readability = self.analyzer.calculate_readability(post.content)
        
        analysis = {
            'platform': post.platform,
            'author': post.author,
            'sentiment': sentiment,
            'sentiment_score': score,
            'top_keywords': keywords,
            'readability_score': round(readability, 2),
            'character_count': len(post.content),
            'hashtag_count': len(post.hashtags),
            'engagement_rate': post.get_engagement_rate()
        }
        
        return analysis
    
    def get_top_posts(self, n=5):
        """Get top N posts by engagement"""
        sorted_posts = sorted(self.posts, key=lambda p: p.get_engagement_rate(), reverse=True)
        return sorted_posts[:n]
    
    def get_platform_stats(self):
        """Get statistics by platform"""
        platform_stats = {}
        
        for post in self.posts:
            if post.platform not in platform_stats:
                platform_stats[post.platform] = {
                    'total_posts': 0,
                    'total_engagement': 0,
                    'sentiments': []
                }
            
            platform_stats[post.platform]['total_posts'] += 1
            platform_stats[post.platform]['total_engagement'] += post.get_engagement_rate()
            sentiment, _ = self.analyzer.analyze_sentiment(post.content)
            platform_stats[post.platform]['sentiments'].append(sentiment)
        
        return platform_stats
    
    def generate_report(self):
        """Generate comprehensive analytics report"""
        print("\n" + "="*60)
        print("📊 SOCIAL MEDIA ANALYTICS REPORT")
        print("="*60)
        
        # Overall statistics
        total_posts = len(self.posts)
        total_engagement = sum(post.get_engagement_rate() for post in self.posts)
        
        print(f"\n📈 Overall Statistics:")
        print(f"   Total Posts: {total_posts}")
        print(f"   Total Engagement: {total_engagement}")
        print(f"   Average Engagement per Post: {total_engagement/total_posts if total_posts > 0 else 0:.2f}")
        
        # Platform breakdown
        print(f"\n🌐 Platform Breakdown:")
        platform_stats = self.get_platform_stats()
        for platform, stats in platform_stats.items():
            print(f"\n   {platform}:")
            print(f"      Posts: {stats['total_posts']}")
            print(f"      Total Engagement: {stats['total_engagement']}")
            sentiment_counts = Counter(stats['sentiments'])
            print(f"      Sentiment: {dict(sentiment_counts)}")
        
        # Top performing posts
        print(f"\n🏆 Top 3 Posts by Engagement:")
        top_posts = self.get_top_posts(3)
        for i, post in enumerate(top_posts, 1):
            print(f"\n   {i}. Platform: {post.platform}")
            print(f"      Author: {post.author}")
            print(f"      Content: {post.content[:50]}...")
            print(f"      Engagement: {post.get_engagement_rate()}")
        
        print("\n" + "="*60)
    
    def save_to_file(self, filename='social_media_data.json'):
        """Save posts to JSON file"""
        data = [post.to_dict() for post in self.posts]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\n💾 Data saved to {filename}")

def demo_usage():
    """Demonstrate the Social Media Manager"""
    
    print("🚀 AI Content Analyzer & Social Media Manager")
    print("=" * 60)
    
    # Create manager instance
    manager = SocialMediaManager()
    
    # Sample posts data
    posts_data = [
        {
            'platform': 'Twitter',
            'content': 'Just launched our amazing new AI product! This is going to revolutionize the industry. Excited to share this with everyone!',
            'author': 'TechStartupCEO',
            'hashtags': ['#AI', '#Innovation', '#TechLaunch'],
            'engagement': {'likes': 245, 'shares': 89, 'comments': 34}
        },
        {
            'platform': 'LinkedIn',
            'content': 'Great insights from today\'s conference on cloud computing and digital transformation. The future is here!',
            'author': 'CloudExpert',
            'hashtags': ['#Cloud', '#DigitalTransformation'],
            'engagement': {'likes': 156, 'shares': 45, 'comments': 23}
        },
        {
            'platform': 'Instagram',
            'content': 'Behind the scenes at our development team. Working hard to build amazing solutions for our customers.',
            'author': 'DevTeamLead',
            'hashtags': ['#DevLife', '#Coding', '#TeamWork'],
            'engagement': {'likes': 389, 'shares': 12, 'comments': 67}
        },
        {
            'platform': 'Twitter',
            'content': 'Disappointed with the latest update. Many bugs and poor performance. Hope this gets fixed soon.',
            'author': 'FrustratedUser',
            'hashtags': ['#TechIssues'],
            'engagement': {'likes': 78, 'shares': 34, 'comments': 56}
        },
        {
            'platform': 'LinkedIn',
            'content': 'Excellent webinar on AWS cloud services and best practices. Learned so much about serverless architecture!',
            'author': 'CloudArchitect',
            'hashtags': ['#AWS', '#Serverless', '#CloudComputing'],
            'engagement': {'likes': 201, 'shares': 67, 'comments': 29}
        }
    ]
    
    # Create posts and add engagement
    print("\n📝 Creating and analyzing posts...\n")
    for data in posts_data:
        post = manager.create_post(
            data['platform'],
            data['content'],
            data['author'],
            data['hashtags']
        )
        post.add_engagement(**data['engagement'])
        
        # Analyze individual post
        analysis = manager.analyze_post(post)
        print(f"\n   Analysis for {data['author']}'s post:")
        print(f"   - Sentiment: {analysis['sentiment']} (score: {analysis['sentiment_score']})")
        print(f"   - Top Keywords: {', '.join([w[0] for w in analysis['top_keywords'][:3]])}")
        print(f"   - Readability Score: {analysis['readability_score']}/100")
        print(f"   - Engagement Rate: {analysis['engagement_rate']}")
    
    # Generate comprehensive report
    manager.generate_report()
    
    # Save data to file
    manager.save_to_file()
    
    print("\n✨ Demo completed successfully!")

# Run the demonstration
if __name__ == "__main__":
    demo_usage()