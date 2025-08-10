import React, { useState } from 'react';
import './QueryForm.css';

interface QueryFormProps {
  onSubmit: (questions: string[]) => void;
  loading: boolean;
}

const QueryForm: React.FC<QueryFormProps> = ({ onSubmit, loading }) => {
  const [questions, setQuestions] = useState<string[]>(['']);

  const addQuestion = () => {
    setQuestions([...questions, '']);
  };

  const removeQuestion = (index: number) => {
    if (questions.length > 1) {
      setQuestions(questions.filter((_, i) => i !== index));
    }
  };

  const updateQuestion = (index: number, value: string) => {
    const updatedQuestions = [...questions];
    updatedQuestions[index] = value;
    setQuestions(updatedQuestions);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    const validQuestions = questions.filter(q => q.trim() !== '');
    if (validQuestions.length === 0) {
      alert('Please enter at least one question');
      return;
    }

    onSubmit(validQuestions);
  };

  return (
    <div className="query-form-container">
      <form onSubmit={handleSubmit} className="query-form">
        <div className="form-group">
          <label>Questions:</label>
          {questions.map((question, index) => (
            <div key={index} className="question-input-group">
              <input
                type="text"
                value={question}
                onChange={(e) => updateQuestion(index, e.target.value)}
                placeholder={`Question ${index + 1}`}
                disabled={loading}
              />
              {questions.length > 1 && (
                <button
                  type="button"
                  onClick={() => removeQuestion(index)}
                  className="remove-question-btn"
                  disabled={loading}
                >
                  ×
                </button>
              )}
            </div>
          ))}
          <button
            type="button"
            onClick={addQuestion}
            className="add-question-btn"
            disabled={loading}
          >
            + Add Another Question
          </button>
        </div>

        <button 
          type="submit" 
          className="submit-btn" 
          disabled={loading}
        >
          {loading ? 'Processing...' : 'Ask Questions'}
        </button>
      </form>
    </div>
  );
};

export default QueryForm;