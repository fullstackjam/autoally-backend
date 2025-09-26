# AutoAlly Backend Helm Chart

Minimal Kubernetes deployment configuration with all values fixed, no complex setup required.

## Quick Start

### Install
```bash
helm install autoally-backend ./autoally-backend
```

### Scale replicas
```bash
helm install autoally-backend ./autoally-backend \
  --set replicaCount=5
```

### Use different image
```bash
helm install autoally-backend ./autoally-backend \
  --set image.tag=v1.0.0
```

### Custom domain
```bash
helm install autoally-backend ./autoally-backend \
  --set ingress.host=your-domain.com
```

## Included Resources

- **Deployment**: AutoAlly Backend FastAPI application (3 replicas by default)
- **Service**: Routes traffic to Pods
- **Ingress**: External access entry point (autoally-backend.fullstackjam.com)

## Fixed Configuration

- **Application Name**: `autoally-backend`
- **Port**: `8000` (FastAPI default)
- **Environment Variables**: SLACK_SIGNING_SECRET and SLACK_BOT_TOKEN from secret

## Configurable Options

| Parameter | Default | Description |
|-----------|---------|-------------|
| `replicaCount` | `3` | Number of Pod replicas |
| `image.repository` | `fullstackjam/autoally-backend` | Image repository |
| `image.tag` | `latest` | Image tag |
| `ingress.host` | `autoally-backend.fullstackjam.com` | Access domain |

## Prerequisites

Before deploying, ensure you have created the required secret:

```bash
kubectl create secret generic autoally-backend-secret \
  --from-literal=SLACK_SIGNING_SECRET=your_slack_signing_secret \
  --from-literal=SLACK_BOT_TOKEN=your_slack_bot_token
```

## Uninstall

```bash
helm uninstall autoally-backend
```
