import Relay from 'react-relay';

export default class extends Relay.Route {
  static queries = {
    rebels: () => Relay.QL`
      query {
        rebels
      }
    `
  };
  static routeName = 'AppHomeRoute';
}
