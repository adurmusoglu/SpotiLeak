import React from 'react';

interface SearchInputProps {
    type: 'artist' | 'song';
    placeholder?: string;
    value?: string;
    onChange?: (value: string) => void;
}

const SearchInput: React.FC<SearchInputProps> = ({
    type, 
    placeholder,
    value,
    onChange
}) => {
    return (
        <div className={`${type}-search-section`}>
            <label htmlFor={`${type}-search`} className="search-label">
                {type === 'artist' ? 'Artist: ' : 'Song: '}
            </label>
            <input
                id={`${type}-search`}
                className={`${type}-search-bar`}
                type="text"
                placeholder={placeholder || `${type.charAt(0).toUpperCase() + type.slice(1)} name`}
                value={value}
                onChange={(e) => onChange?.(e.target.value)}
            />
        </div>
    )
}

export default SearchInput;