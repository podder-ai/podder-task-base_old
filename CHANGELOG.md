# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/).

# [0.9.1]
### Changed
- [PA-3111] Stop using logger class from TaskApiExecutor to avoid duplicate log outputs

# [0.9.0]
### Changed
- [PA-3111] Enable configuring the path to the `pipeline.yml` file

# [0.8.2]
### Changed
- [PA-2858] Fix gRPC error by shortening gRPC server's TCP connection keep alive

# [0.8.1]
### Changed
- [PA-2516] Setting Mysql session pool_size, max_overflow using `GRPC_MAX_WORKERS` from settings

## [0.8.0]
### Changes
- [PA-2498] Change to stop grpc_server.py when SIGTERM signal received.

## [0.7.1]
### Fix
- [PA-2501] Fix base repository to ensure commit and rollback for database

## [0.7.0]
### Add
- [PA-2247] Set the maximum number of grpc requests in order not to accept requests during processing

## [0.6.1]
### Add
- [PA-2488] Add handling of exception which occurred on task

## [0.6.0]
### Add
- Add CHANGELOG.md file.

### Changes
- [PA-1399] Fix dependency of libraries
- [PA-1347] Refactor task grpc server
