# Component Template

A reusable React component starter with TypeScript, tests, and Storybook support.

## Quick Start

```bash
cp -r accelerators/dev/templates/component src/components/<REPLACE_COMPONENT_NAME>
# Rename files and replace placeholders
```

## Files

### `<REPLACE_COMPONENT_NAME>.tsx`

```tsx
import React from 'react';
import styles from './<REPLACE_COMPONENT_NAME>.module.css';

export interface <REPLACE_COMPONENT_NAME>Props {
  /** <REPLACE_PROP_DESCRIPTION> */
  label: string;
  onClick?: () => void;
}

const <REPLACE_COMPONENT_NAME>: React.FC<<REPLACE_COMPONENT_NAME>Props> = ({
  label,
  onClick,
}) => (
  <button className={styles.root} onClick={onClick} type="button">
    {label}
  </button>
);

export default <REPLACE_COMPONENT_NAME>;
```

### `<REPLACE_COMPONENT_NAME>.module.css`

```css
.root {
  /* <REPLACE_STYLES> */
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```

### `<REPLACE_COMPONENT_NAME>.test.tsx`

```tsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import <REPLACE_COMPONENT_NAME> from './<REPLACE_COMPONENT_NAME>';

describe('<REPLACE_COMPONENT_NAME>', () => {
  it('renders the label', () => {
    render(<<REPLACE_COMPONENT_NAME> label="Click me" />);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick when clicked', () => {
    const handler = jest.fn();
    render(<<REPLACE_COMPONENT_NAME> label="Click me" onClick={handler} />);
    fireEvent.click(screen.getByRole('button'));
    expect(handler).toHaveBeenCalledTimes(1);
  });
});
```

### `<REPLACE_COMPONENT_NAME>.stories.tsx`

```tsx
import type { Meta, StoryObj } from '@storybook/react';
import <REPLACE_COMPONENT_NAME> from './<REPLACE_COMPONENT_NAME>';

const meta: Meta<typeof <REPLACE_COMPONENT_NAME>> = {
  title: 'Components/<REPLACE_COMPONENT_NAME>',
  component: <REPLACE_COMPONENT_NAME>,
};
export default meta;

type Story = StoryObj<typeof <REPLACE_COMPONENT_NAME>>;

export const Default: Story = {
  args: { label: 'Button' },
};
```

## Placeholders Reference

| Placeholder | Description |
|-------------|-------------|
| `<REPLACE_COMPONENT_NAME>` | PascalCase component name |
| `<REPLACE_PROP_DESCRIPTION>` | JSDoc description for the main prop |
| `<REPLACE_STYLES>` | Base CSS styles |
