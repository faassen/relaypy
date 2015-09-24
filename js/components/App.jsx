import React from 'react';
import Relay from 'react-relay';

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>Ship list</h1>
        <ul>
          {this.props.rebels.ships.edges.map(edge =>
            <li>{edge.node.name} (ID: {edge.node.id})</li>
          )}
        </ul>
      </div>
    );
  }
}

export default Relay.createContainer(App, {
  fragments: {
    viewer: () => Relay.QL`
      fragment on Faction {
        ships(first: 10) {
          edges {
            node {
              id,
              name,
            },
          },
        },
      }
    `
  }
});
