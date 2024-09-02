import { render, fireEvent } from '@testing-library/react';
import App from './App';
import { act } from 'react';

describe('App component', () => {
  test('initial button text is "Click me"', () => {
    const { getByText } = render(<App />);
    const button = getByText('Click me');
    expect(button).toBeInTheDocument();
  });

  test('button text changes to "Button Clicked!" after click', () => {
    const { getByText } = render(<App />);
    const button = getByText('Click me');
    fireEvent.click(button);
    expect(getByText('Button Clicked!')).toBeInTheDocument();
  });

  test('greetings button initially has text "Greetings"', () => {
    const { getByText } = render(<App />);
    const greetingButton = getByText('Greetings');
    expect(greetingButton).toBeInTheDocument();
  });
});
