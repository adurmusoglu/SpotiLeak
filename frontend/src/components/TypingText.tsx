import React, { useState, useEffect } from "react";

interface TypingTextProps {
  lines: string[];
  speed?: number;
  className?: string;
}

const TypingText: React.FC<TypingTextProps> = ({ lines, speed = 50, className }) => {
  const [displayLines, setDisplayLines] = useState<string[]>(new Array(lines.length).fill(""));
  const [currentLineIndex, setCurrentLineIndex] = useState(0);
  const [currentCharIndex, setCurrentCharIndex] = useState(0);

  useEffect(() => {
    if (currentLineIndex >= lines.length) return;

    const timer = setInterval(() => {
      const currentLine = lines[currentLineIndex];
      
      if (currentCharIndex < currentLine.length) {
        setDisplayLines(prev => {
          const newLines = [...prev];
          newLines[currentLineIndex] = currentLine.substring(0, currentCharIndex + 1);
          return newLines;
        });
        setCurrentCharIndex(prev => prev + 1);
      } else {
        // Line is complete, move to next line
        setCurrentLineIndex(prev => prev + 1);
        setCurrentCharIndex(0);
        clearInterval(timer);
      }
    }, speed);

    return () => clearInterval(timer);
  }, [currentLineIndex, currentCharIndex, lines, speed]);

  return (
    <div className={className}>
      {lines.map((line, index) => (
        <p key={index} style={{ 
          visibility: index < currentLineIndex || (index === currentLineIndex && displayLines[index]) ? 'visible' : 'hidden',
          minHeight: '1.92rem' // Ensures consistent line height
        }}>
          {displayLines[index] || line}
        </p>
      ))}
    </div>
  );
};

export default TypingText;