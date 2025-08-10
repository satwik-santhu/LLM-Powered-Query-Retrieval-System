import React from 'react';
import './ResponseDisplay.css';

interface QueryResponse {
  answers: string[];
}

interface ResponseDisplayProps {
  response: QueryResponse | null;
  loading: boolean;
  error: string;
}

const ResponseDisplay: React.FC<ResponseDisplayProps> = ({ response, loading, error }) => {
  if (loading) {
    return (
      <div className="response-container">
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Processing your questions...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="response-container">
        <div className="error-message">
          <h3>Error</h3>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  if (!response) {
    return (
      <div className="response-container">
        <div className="placeholder">
          <p>Submit your questions to see answers here</p>
        </div>
      </div>
    );
  }

  return (
    <div className="response-container">
      <h3>Answers</h3>
      <div className="answers-list">
        {response.answers.map((answer, index) => (
          <div key={index} className="answer-item">
            <div className="answer-header">
              <span className="answer-number">Answer {index + 1}</span>
            </div>
            <div className="answer-content">
              <p>{answer}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ResponseDisplay;